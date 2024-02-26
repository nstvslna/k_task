xx = int(input("Введіть кількість хвилин, необхідних вам для сну: "))
print("Введіть час, коли ви заснули (перше введіть години, а потім - хвилини): ")
hh = int(input())
mm = int(input())
# Розрахунок часу пробудження
time_to_sleep = hh * 60 + mm
time_to_wake_up = time_to_sleep + xx
# Розрахунок годин і хвилин для будильника
hh_time_to_wake_up = time_to_wake_up // 60
mm_time_to_wake_up = time_to_wake_up % 60
# Виведення результату
print("Вам потрібно поставити будильник на: ")
print(hh_time_to_wake_up, "год")
print(mm_time_to_wake_up, "хв")