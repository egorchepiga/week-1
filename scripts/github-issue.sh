#!/bin/bash
#
# GitHub Issue Creator/Updater
# Создаёт или обновляет Issue для текущей ветки
#
# Использование: ./scripts/github-issue.sh "Краткое описание что сделано"
#

set -e

# Конфигурация
GITHUB_TOKEN="${GITHUB_TOKEN:-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}"
REPO_OWNER="egorchepiga"
REPO_NAME="week-1"
API_URL="https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}"

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Получаем текущую ветку
BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ -z "$BRANCH" ]; then
    echo -e "${RED}Error: Could not determine current branch${NC}"
    exit 1
fi

# Описание из аргумента или дефолтное
SUMMARY="${1:-Session update}"

# Формируем заголовок
TITLE="[${BRANCH}] ${SUMMARY}"

# Читаем SESSION_LOG.md если существует
SESSION_LOG_PATH="$(git rev-parse --show-toplevel)/SESSION_LOG.md"
if [ -f "$SESSION_LOG_PATH" ]; then
    SESSION_LOG=$(cat "$SESSION_LOG_PATH")
else
    SESSION_LOG="No SESSION_LOG.md found"
fi

# Формируем body
BODY=$(cat <<EOF
## Branch
\`${BRANCH}\`

**Link:** [View Branch](https://github.com/${REPO_OWNER}/${REPO_NAME}/tree/${BRANCH})

---

## Session Log

${SESSION_LOG}

---

*Updated automatically by github-issue.sh*
EOF
)

# Экранируем JSON
escape_json() {
    python3 -c "import json,sys; print(json.dumps(sys.stdin.read()))" <<< "$1"
}

TITLE_JSON=$(escape_json "$TITLE")
BODY_JSON=$(escape_json "$BODY")

# Ищем существующий Issue по ветке
echo -e "${YELLOW}Searching for existing issue for branch: ${BRANCH}${NC}"

SEARCH_RESULT=$(curl -s -H "Authorization: token ${GITHUB_TOKEN}" \
    -H "Accept: application/vnd.github.v3+json" \
    "${API_URL}/issues?state=all&per_page=100")

# Ищем Issue с названием ветки в заголовке
EXISTING_ISSUE=$(echo "$SEARCH_RESULT" | python3 -c "
import json, sys
data = json.load(sys.stdin)
branch = '${BRANCH}'
for issue in data:
    if isinstance(issue, dict) and branch in issue.get('title', ''):
        print(issue['number'])
        break
" 2>/dev/null || echo "")

if [ -n "$EXISTING_ISSUE" ] && [ "$EXISTING_ISSUE" != "" ]; then
    # Обновляем существующий Issue
    echo -e "${YELLOW}Found existing issue #${EXISTING_ISSUE}, updating...${NC}"

    RESPONSE=$(curl -s -X PATCH \
        -H "Authorization: token ${GITHUB_TOKEN}" \
        -H "Accept: application/vnd.github.v3+json" \
        "${API_URL}/issues/${EXISTING_ISSUE}" \
        -d "{\"title\": ${TITLE_JSON}, \"body\": ${BODY_JSON}}")

    ISSUE_URL=$(echo "$RESPONSE" | python3 -c "import json,sys; print(json.load(sys.stdin).get('html_url', 'Error'))" 2>/dev/null || echo "Error")

    if [ "$ISSUE_URL" != "Error" ] && [ -n "$ISSUE_URL" ]; then
        echo -e "${GREEN}Issue updated successfully!${NC}"
        echo -e "URL: ${ISSUE_URL}"
    else
        echo -e "${RED}Error updating issue${NC}"
        echo "$RESPONSE"
        exit 1
    fi
else
    # Создаём новый Issue
    echo -e "${YELLOW}No existing issue found, creating new...${NC}"

    RESPONSE=$(curl -s -X POST \
        -H "Authorization: token ${GITHUB_TOKEN}" \
        -H "Accept: application/vnd.github.v3+json" \
        "${API_URL}/issues" \
        -d "{\"title\": ${TITLE_JSON}, \"body\": ${BODY_JSON}, \"labels\": [\"week-1\", \"auto-generated\"]}")

    ISSUE_URL=$(echo "$RESPONSE" | python3 -c "import json,sys; print(json.load(sys.stdin).get('html_url', 'Error'))" 2>/dev/null || echo "Error")

    if [ "$ISSUE_URL" != "Error" ] && [ -n "$ISSUE_URL" ]; then
        echo -e "${GREEN}Issue created successfully!${NC}"
        echo -e "URL: ${ISSUE_URL}"
    else
        echo -e "${RED}Error creating issue${NC}"
        echo "$RESPONSE"
        exit 1
    fi
fi

echo -e "${GREEN}Done!${NC}"
