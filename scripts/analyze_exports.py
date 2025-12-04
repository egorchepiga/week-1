import pandas as pd
import os
import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

folder = r'C:\Users\George\Desktop\startup\app-database'
all_data = []

for f in os.listdir(folder):
    if f.endswith('.xlsx'):
        path = os.path.join(folder, f)
        try:
            df = pd.read_excel(path, skiprows=1)  # Skip first row (header info)
            all_data.append(df)
        except:
            pass

combined = pd.concat(all_data, ignore_index=True)

# Rename columns properly
combined.columns = ['Logo', 'Title', 'Users', 'ID', 'Version', 'Rating', 'Reviews',
                    'Manifest', 'Lang', 'Categories', 'Featured', 'Trader',
                    'Website', 'Email', 'Size', 'Updated', 'Added'] + list(combined.columns[17:])

# Keep only main columns
df = combined[['Title', 'Users', 'ID', 'Rating', 'Reviews', 'Lang', 'Categories', 'Website']].copy()

# Remove duplicates and NaN titles
df = df.dropna(subset=['Title'])
df = df.drop_duplicates(subset=['Title'])

# Convert Users to numeric
def parse_users(val):
    if pd.isna(val):
        return 0
    val = str(val).replace(',', '').replace(' ', '')
    if 'M' in val or 'm' in val:
        return int(float(val.replace('M', '').replace('m', '')) * 1000000)
    if 'K' in val or 'k' in val:
        return int(float(val.replace('K', '').replace('k', '')) * 1000)
    try:
        return int(val)
    except:
        return 0

df['Users_Num'] = df['Users'].apply(parse_users)
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

# Sort by users
df = df.sort_values('Users_Num', ascending=False)

# Count languages
def count_langs(val):
    if pd.isna(val):
        return 0
    return len(str(val).split(','))

df['Lang_Count'] = df['Lang'].apply(count_langs)

print("=" * 80)
print("АНАЛИЗ ЭКСПОРТА APP-DATABASE")
print("=" * 80)
print(f"\nВсего уникальных расширений: {len(df)}")

print("\n" + "=" * 80)
print("ТОП-50 ПО КОЛИЧЕСТВУ ПОЛЬЗОВАТЕЛЕЙ")
print("=" * 80)
for i, row in df.head(50).iterrows():
    users = row['Users_Num']
    if users >= 1000000:
        users_str = f"{users/1000000:.1f}M"
    elif users >= 1000:
        users_str = f"{users/1000:.0f}K"
    else:
        users_str = str(users)

    rating = row['Rating'] if pd.notna(row['Rating']) else 0
    reviews = int(row['Reviews']) if pd.notna(row['Reviews']) else 0
    langs = row['Lang_Count']

    print(f"{users_str:>8} | ★{rating:.1f} | {reviews:>6} reviews | {langs:>2} langs | {row['Title'][:60]}")

# AI-related extensions
print("\n" + "=" * 80)
print("AI/CHATGPT РАСШИРЕНИЯ")
print("=" * 80)
ai_keywords = ['ai', 'chatgpt', 'gpt', 'openai', 'gemini', 'claude', 'copilot', 'artificial']
ai_df = df[df['Title'].str.lower().str.contains('|'.join(ai_keywords), na=False)]
ai_df = ai_df.sort_values('Users_Num', ascending=False)

for i, row in ai_df.head(30).iterrows():
    users = row['Users_Num']
    if users >= 1000000:
        users_str = f"{users/1000000:.1f}M"
    elif users >= 1000:
        users_str = f"{users/1000:.0f}K"
    else:
        users_str = str(users)

    rating = row['Rating'] if pd.notna(row['Rating']) else 0
    langs = row['Lang_Count']

    print(f"{users_str:>8} | ★{rating:.1f} | {langs:>2} langs | {row['Title'][:65]}")

# GitHub/Developer extensions
print("\n" + "=" * 80)
print("DEVELOPER/GITHUB РАСШИРЕНИЯ")
print("=" * 80)
dev_keywords = ['github', 'developer', 'code', 'json', 'react', 'debug', 'api', 'git']
dev_df = df[df['Title'].str.lower().str.contains('|'.join(dev_keywords), na=False)]
dev_df = dev_df.sort_values('Users_Num', ascending=False)

for i, row in dev_df.head(20).iterrows():
    users = row['Users_Num']
    if users >= 1000000:
        users_str = f"{users/1000000:.1f}M"
    elif users >= 1000:
        users_str = f"{users/1000:.0f}K"
    else:
        users_str = str(users)

    rating = row['Rating'] if pd.notna(row['Rating']) else 0
    langs = row['Lang_Count']

    print(f"{users_str:>8} | ★{rating:.1f} | {langs:>2} langs | {row['Title'][:65]}")

# LinkedIn/Social extensions
print("\n" + "=" * 80)
print("LINKEDIN/SOCIAL РАСШИРЕНИЯ")
print("=" * 80)
social_keywords = ['linkedin', 'twitter', 'social', 'facebook', 'instagram']
social_df = df[df['Title'].str.lower().str.contains('|'.join(social_keywords), na=False)]
social_df = social_df.sort_values('Users_Num', ascending=False)

for i, row in social_df.head(15).iterrows():
    users = row['Users_Num']
    if users >= 1000000:
        users_str = f"{users/1000000:.1f}M"
    elif users >= 1000:
        users_str = f"{users/1000:.0f}K"
    else:
        users_str = str(users)

    rating = row['Rating'] if pd.notna(row['Rating']) else 0
    langs = row['Lang_Count']

    print(f"{users_str:>8} | ★{rating:.1f} | {langs:>2} langs | {row['Title'][:65]}")

# Potential opportunities (high users, low ratings, few langs)
print("\n" + "=" * 80)
print("ПОТЕНЦИАЛЬНЫЕ ВОЗМОЖНОСТИ (много пользователей, низкий рейтинг или мало языков)")
print("=" * 80)
opportunities = df[(df['Users_Num'] >= 100000) & ((df['Rating'] < 4.0) | (df['Lang_Count'] < 10))]
opportunities = opportunities.sort_values('Users_Num', ascending=False)

for i, row in opportunities.head(20).iterrows():
    users = row['Users_Num']
    if users >= 1000000:
        users_str = f"{users/1000000:.1f}M"
    elif users >= 1000:
        users_str = f"{users/1000:.0f}K"
    else:
        users_str = str(users)

    rating = row['Rating'] if pd.notna(row['Rating']) else 0
    langs = row['Lang_Count']

    print(f"{users_str:>8} | ★{rating:.1f} | {langs:>2} langs | {row['Title'][:60]}")

# Save full analysis
output = os.path.join(folder, 'analysis_report.csv')
df.to_csv(output, index=False, encoding='utf-8')
print(f"\n\nПолный отчёт сохранён: {output}")
