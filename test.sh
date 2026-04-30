#!/usr/bin/env bash
set -uo pipefail
RED='\033[0;31m'; GREEN='\033[0;32m'; NC='\033[0m'
PASS=0; FAIL=0

[[ -z "${SYNAPSE_API_KEY:-}" ]] && echo "Set SYNAPSE_API_KEY" && exit 1

echo "Installing..."
pip install -q -r requirements.txt 2>&1 | tail -1 > /dev/null 2>&1

run_script() {
  local name="$1" cmd="$2"
  if eval "$cmd" > /dev/null 2>&1; then
    echo -e "  ${GREEN}✓${NC} $name"
    ((PASS++)) || true
  else
    echo -e "  ${RED}✗${NC} $name"
    ((FAIL++)) || true
  fi
}

echo "Running all scripts..."

echo "── Core ──"
run_script "track_event" "python3 track_event.py"
run_script "track_batch" "python3 track_batch.py"
run_script "identify_contact" "python3 identify_contact.py"
run_script "identify_batch" "python3 identify_batch.py"
run_script "send_email" "python3 send_email.py"
run_script "async_example" "python3 async_example.py"

echo "── Contacts ──"
run_script "contacts_list" "python3 contacts_list.py"
run_script "contacts_get" "python3 contacts_get.py"
run_script "contacts_update" "python3 contacts_update.py"
run_script "contacts_delete" "python3 contacts_delete.py"

echo "── Templates ──"
run_script "templates_list" "python3 templates_list.py"
run_script "templates_get" "python3 templates_get.py"
run_script "templates_create" "python3 templates_create.py"
run_script "templates_update" "python3 templates_update.py"
run_script "templates_preview" "python3 templates_preview.py"
run_script "templates_delete" "python3 templates_delete.py"

echo ""
echo "Results: $PASS passed, $FAIL failed"
[[ $FAIL -eq 0 ]] && echo -e "${GREEN}All passed!${NC}" || echo -e "${RED}$FAIL failed${NC}"
exit $FAIL
