import os
import shutil

mapping = {
    'a4ed6a2e-1fd6-41b2-b842-135e0cbe8f29': '01_vybor_idei',
    '052b934e-42bf-4470-ae6a-7f15b5a04f2b': '02_ocenka_dohodnosti',
    '68efd39d-f277-4fa0-b05c-181bf6b43d7e': '03_podschet_ballov',
    '1aff94d0-db25-4d73-aac2-79c0a1072643': '04_podbor_zaprosa_1',
    'c3aeb0aa-3827-4910-9567-e2da9cf1298b': '05_podbor_zaprosa_2',
    '7a348df5-717e-48d4-831d-d0501590caa4': '06_keyword_difficulty',
    '9dab90f7-bc6b-4fe5-90bf-876e5f8d3a34': '07_proverka_konkurentov',
    '4ffdeaae-0a95-4cff-a43b-d35b4722475f': '08_ranzhirovanie_po_zaprosam',
    'ede332c2-da77-40c5-a6f0-2634f17fe228': '09_proverka_klucha',
    '3506679c-6d7d-4cd0-a251-d51eaaf5950e': '10_vytaskivaem_funkciyu',
    'ed44d2f3-fd58-46db-afa7-dbe64f0760fc': '11_otpravka_rezultatov'
}

base_dir = r'C:\Users\George\Desktop\startup\builds-html\I'

for old_id, new_name in mapping.items():
    old_htm = os.path.join(base_dir, f'{old_id}.htm')
    new_htm = os.path.join(base_dir, f'{new_name}.htm')

    old_files = os.path.join(base_dir, f'{old_id}_files')
    new_files = os.path.join(base_dir, f'{new_name}_files')

    if os.path.exists(old_htm):
        os.rename(old_htm, new_htm)
        print(f'Renamed: {old_id}.htm -> {new_name}.htm')

    if os.path.exists(old_files):
        os.rename(old_files, new_files)
        print(f'Renamed: {old_id}_files -> {new_name}_files')

print('Done!')
