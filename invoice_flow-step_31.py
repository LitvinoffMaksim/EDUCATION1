# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: InvoiceFlow
def switch_profile(current_profile: str, new_profile: str) -> None:
    profiles = get_all_profiles()
    if current_profile not in profiles:
        raise ValueError(f"Профиль '{current_profile}' не найден")
    if new_profile not in profiles:
        raise ValueError(f"Профиль '{new_profile}' не найден")
    profiles[current_profile]["active"] = False
    profiles[new_profile]["active"] = True
    save_profiles(profiles)
    print(f"Переключено на профиль: {new_profile}")
