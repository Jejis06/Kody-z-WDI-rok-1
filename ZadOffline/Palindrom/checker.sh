#!/bin/bash

# --- KONFIGURACJA ---
PROGRAM=$1
TRYB=$2  # Drugi argument: opcjonalnie 'stop'
TEST_DIR="testy"
KATEGORIE=("male" "srednie" "duze")
TEMP_OUT="temp.user.out"

# --- KOLORY I STYLE ---
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Kolory dla grup
CYAN='\033[0;36m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
BOLD='\033[1m'

# --- SPRAWDZENIE ARGUMENTÓW ---
if [ -z "$PROGRAM" ]; then
    echo -e "${RED}Błąd: Nie podano pliku programu (.py).${NC}"
    echo "Użycie: ./tester.sh plik.py [stop]"
    exit 1
fi

if [ ! -f "$PROGRAM" ]; then
    echo -e "${RED}Błąd: Plik '$PROGRAM' nie istnieje.${NC}"
    exit 1
fi

# --- GŁÓWNA PĘTLA PO KATEGORIACH ---
for KAT in "${KATEGORIE[@]}"; do
    FULL_PATH="$TEST_DIR/$KAT"
    
    # Ustawienie stylu w zależności od kategorii
    case $KAT in
        "male")
            THEME_COLOR=$CYAN
            ICON="🌱"
            HEADER="=== TESTY MAŁE ==="
            ;;
        "srednie")
            THEME_COLOR=$BLUE
            ICON="🚀"
            HEADER="::: TESTY ŚREDNIE :::"
            ;;
        "duze")
            THEME_COLOR=$MAGENTA
            ICON="🔥"
            HEADER="### TESTY DUŻE ###"
            ;;
    esac

    # Wyświetlenie nagłówka grupy
    echo -e "\n${THEME_COLOR}${BOLD}${HEADER}${NC}"
    
    if [ ! -d "$FULL_PATH" ]; then
        echo "Katalog $FULL_PATH nie istnieje, pomijam."
        continue
    fi

    COUNT=0
    PASSED=0

    # Pętla po plikach .in
    for IN_FILE in "$FULL_PATH/in"/*.in; do
        [ -e "$IN_FILE" ] || continue
        ((COUNT++))
        
        BASENAME=$(basename "$IN_FILE" .in)
        OUT_FILE="$FULL_PATH/out/$BASENAME.out"

        if [ ! -f "$OUT_FILE" ]; then
            echo -e "${ICON} Test ${BASENAME}: ${YELLOW}BRAK PLIKU OUT${NC}"
            continue
        fi

        # --- POMIAR CZASU I URUCHOMIENIE PYTHON ---
        TS=$(date +%s%N)
        
        # Uruchomienie programu w Pythonie
        python3 "$PROGRAM" 0 < "$IN_FILE" > "$TEMP_OUT"
        
        TE=$(date +%s%N)
        ELAPSED=$(( (TE - TS) / 1000000 ))

        # --- WERYFIKACJA ---
        if diff -w "$TEMP_OUT" "$OUT_FILE" > /dev/null; then
            # Sukces - wypisanie w kolorze grupy lub zielonym
            echo -e "${THEME_COLOR}[${KAT}]${NC} Test ${BASENAME}: ${GREEN}OK${NC} (${ELAPSED}ms)"
            ((PASSED++))
        else
            # Błąd
            echo -e "${THEME_COLOR}[${KAT}]${NC} Test ${BASENAME}: ${RED}BŁĄD${NC} (${ELAPSED}ms)"
            echo -e "${RED}   Oczekiwano innego wyniku!${NC}"
	    python3 "$PROGRAM" 1 < "$IN_FILE"
	    echo ' ans ======== '
	    cat "$OUT_FILE"
            
            # Obsługa zatrzymania programu
            if [ "$TRYB" == "stop" ]; then
                echo -e "\n${RED}!!! Zatrzymano na żądanie (tryb stop) !!!${NC}"
                echo "Różnice (Twój wynik < vs > Oczekiwany):"
                diff -w "$TEMP_OUT" "$OUT_FILE" | head -n 10
                rm -f "$TEMP_OUT"
                exit 1
            fi
        fi
    done

    # Podsumowanie sekcji z odpowiednim formatowaniem
    if [ "$COUNT" -gt 0 ]; then
        echo -e "${THEME_COLOR}Wynik ${KAT}: $PASSED / $COUNT${NC}"
    fi
done

# --- KONIEC ---
rm -f "$TEMP_OUT"
echo -e "\nZakończono wszystkie testy."
