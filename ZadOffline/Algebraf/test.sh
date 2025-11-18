#!/bin/bash

# --- Konfiguracja ---
SOLVER_NAME="ultrafast.py"     # Nazwa Twojego programu
GENERATOR_NAME="generator.py" # Nazwa generatora
PYTHON_CMD="python3"

# Liczba testów do uruchomienia (możesz podać jako argument)
NUM_TESTS=${1:-10}

# --- Liczniki i kolory ---
PASSED_COUNT=0
TOTAL_TIME=0.0
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m' # Brak koloru

# --- Sprawdzenie plików ---
if [ ! -f "$SOLVER_NAME" ]; then
    echo -e "${RED}BŁĄD: Nie znaleziono programu '$SOLVER_NAME'.${NC}"
    exit 1
fi
if [ ! -f "$GENERATOR_NAME" ]; then
    echo -e "${RED}BŁĄD: Nie znaleziono generatora '$GENERATOR_NAME'.${NC}"
    exit 1
fi
# Sprawdzenie, czy 'bc' (do obliczeń) jest zainstalowany
if ! command -v bc &> /dev/null; then
    echo -e "${RED}BŁĄD: Wymagany program 'bc' nie jest zainstalowany.${NC}"
    exit 1
fi
# Sprawdzenie, czy mamy precyzyjny 'date' (Linux vs macOS)
DATE_CMD="date"
if command -v gdate &> /dev/null; then
    DATE_CMD="gdate" # Użyj gdate na macOS dla nanosekund
fi

echo -e "${YELLOW}Uruchamianie $NUM_TESTS losowych testów dla '$SOLVER_NAME'...${NC}"
echo "-----------------------------------------------------"

for (( i=1; i<=$NUM_TESTS; i++ ))
do
    echo -n -e "Test $i/$NUM_TESTS... "
    
    # 1. Wygeneruj test i oddziel oczekiwany wynik od wejścia
    GENERATOR_OUTPUT=$($PYTHON_CMD "$GENERATOR_NAME")
    
    # Pierwsza linia to oczekiwany wynik
    EXPECTED_OUTPUT=$(echo "$GENERATOR_OUTPUT" | head -n 1)
    
    # Reszta to dane wejściowe dla programu
    TEST_INPUT=$(echo "$GENERATOR_OUTPUT" | tail -n +2)

    # 2. Uruchom program z pomiarem czasu (precyzyjnym)
    START_TIME=$($DATE_CMD +%s.%N)
    ACTUAL_OUTPUT=$(echo -e "$TEST_INPUT" | $PYTHON_CMD "$SOLVER_NAME")
    END_TIME=$($DATE_CMD +%s.%N)

    # Oblicz czas trwania
    DURATION=$(echo "$END_TIME - $START_TIME" | bc)

    # 3. Sprawdź poprawność
    if [ "$ACTUAL_OUTPUT" == "$EXPECTED_OUTPUT" ]; then
        echo -e "${GREEN}PASS${NC} (Czas: ${YELLOW}${DURATION}s${NC})"
        ((PASSED_COUNT++))
        TOTAL_TIME=$(echo "$TOTAL_TIME + $DURATION" | bc)
	#echo $TEST_INPUT
    else
        echo -e "${RED}FAIL${NC} (Czas: ${DURATION}s)"
        echo "  WEJŚCIE:"
        echo "$TEST_INPUT" | sed 's/^/    /' # Wcięcie dla czytelności
        echo "  OCZEKIWANO: '$EXPECTED_OUTPUT'"
        echo "  OTRZYMANO:  '$ACTUAL_OUTPUT'"
    fi
done

echo "-----------------------------------------------------"
echo -e "${YELLOW}Podsumowanie:${NC}"
echo -e "Zaliczono: ${GREEN}$PASSED_COUNT/$NUM_TESTS${NC}"

# Oblicz średni czas tylko dla udanych testów
if (( $(echo "$PASSED_COUNT > 0" | bc -l) )); then
    AVG_TIME=$(echo "scale=4; $TOTAL_TIME / $PASSED_COUNT" | bc)
    echo -e "Całkowity czas (udanych): ${YELLOW}${TOTAL_TIME}s${NC}"
    echo -e "Średni czas (udanych):   ${YELLOW}${AVG_TIME}s${NC}"
fi
