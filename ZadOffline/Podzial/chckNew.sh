#!/bin/bash

PYTHON_SCRIPT="$1"
offpoints=0

declare -a tests_name
declare -a tests_input
declare -a tests_output
declare -a tests_points

# --- TEST CASE 0 ---
tests_name+=("Test 0")
tests_input+=("1374121319 ")
tests_output+=("5")
tests_points+=("0")

# --- TEST CASE 1 ---
tests_name+=("Test 1")
tests_input+=("13171923293137414347 ")
tests_output+=("9") 
tests_points+=("20")

# --- TEST CASE 2 ---
tests_name+=("Test 2")
tests_input+=("12773237131577691975 ")
tests_output+=("8") 
tests_points+=("20")

# --- TEST CASE 3 ---
tests_name+=("Test 3")
tests_input+=("1277323713157769197157122291333 ")
tests_output+=("14") 
tests_points+=("20")

# --- TEST CASE 4 ---
tests_name+=("Test 4")
tests_input+=("9378159283461283135311193412718751359151238745 ")
tests_output+=("BRAK") 
tests_points+=("20")

# --- TEST CASE 5 ---
tests_name+=("Test 5")
tests_input+=("2222222333333335555555555577777777777771313131313131323232323235757575 ")
tests_output+=("55") 
tests_points+=("20")

# --- TEST CASE OFF zlosliwy ---
tests_name+=("Test OFF 0")
tests_input+=("373737373737373737373737373737373737373737373737373737373737373737373737373737373737373737373737373 ")
tests_output+=("50") 
tests_points+=("0")



BOLD='\033[1m'
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m' 
HR="${BLUE}---------------------------------------------------------------------------------${NC}"

# Check if python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo -e "${RED}Error: Could not find file '$PYTHON_SCRIPT'${NC}"
    exit 1
fi

run_with_timeout() {
    local time=$1
    shift
    if command -v timeout &> /dev/null; then
        timeout "${time}s" "$@"
    elif command -v gtimeout &> /dev/null; then
        gtimeout "${time}s" "$@"
    else
        perl -e 'alarm shift; exec @ARGV' "$time" "$@"
    fi
}

echo -e ""
echo -e "${BOLD}Running tests for: ${YELLOW}$PYTHON_SCRIPT${NC}"
echo -e "$HR"
printf "${BOLD}%-15s %-10s %-15s %-10s %-10s${NC}\n" "TEST NAME" "STATUS" "TIME (s)" "SCORE" "MAX PTS"
echo -e "$HR"

passed_count=0
total_count=${#tests_name[@]}
total_score=0
max_possible_score=0

for i in "${!tests_name[@]}"; do
    t_name="${tests_name[$i]}"
    t_input="${tests_input[$i]}"
    t_expected="${tests_output[$i]}"
    t_points="${tests_points[$i]}"
    
    max_possible_score=$(echo "$max_possible_score + $t_points" | bc)

    start_time=$(date +%s%N)

    t_actual_raw=$(echo "$t_input" | run_with_timeout 10s python3 "$PYTHON_SCRIPT")
    exit_code=$?

    end_time=$(date +%s%N)
    
    t_actual=$(echo "$t_actual_raw" | tr -d '[:space:]')
    clean_expected=$(echo "$t_expected" | tr -d '[:space:]')

    duration=$(echo "scale=3; ($end_time - $start_time) / 1000000000" | bc)
    
    time_color=$CYAN
    status=""
    status_color=""
    earned_points=0

    if [ $exit_code -eq 124 ]; then
        status="TIMEOUT"
        status_color=$RED
        time_color=$RED
        t_actual="(Process Killed)"
        duration=10.000
        earned_points=0
    elif [ "$t_actual" == "$clean_expected" ]; then
        status="PASS"
        status_color=$GREEN
        earned_points=$t_points
        
        if (( $(echo "$duration > 1" | bc -l) )); then time_color=$YELLOW; fi
        ((passed_count++))
    else
        status="FAIL"
        status_color=$RED
        earned_points=0
    fi

    printf "%-15s ${status_color}%-10s${NC} ${time_color}%-15s${NC} ${MAGENTA}%-10s${NC} %-10s\n" "${t_name:0:13}" "$status" "$duration" "$earned_points" "$t_points"
    
    total_score=$(echo "$total_score + $earned_points" | bc)

    if [ "$status" == "FAIL" ]; then
        echo -e "${YELLOW}  [Input]:    ${NC}$t_input"
        echo -e "${RED}  [Expected]: ${NC}$clean_expected"
        echo -e "${RED}  [Actual]:   ${NC}$t_actual"
        echo -e "$HR"
    fi
done

echo -e "$HR"

echo -e "${BOLD}SUMMARY:${NC}"
if [ "$passed_count" -eq "$total_count" ]; then
    echo -e "Tests Passed: ${GREEN}$passed_count/$total_count${NC}"
else
    echo -e "Tests Passed: ${RED}$passed_count/$total_count${NC}"
fi

echo -e "Total Score:  ${MAGENTA}$total_score / $max_possible_score${NC}"
echo -e ""
