import random  #random để chọn số ngẫu nhiên
print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100. Try to guess it!")
#chọn ngẫu nhiên 1 số trong khoảng 1..100
secret_number = random.randint(1, 100)
#đếm số lần đoán
attempts = 0
while True:
    try:
        #người chơi nhập số chuyển từ chuỗi sang int
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        #check if số ngoài phạm vi
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100!")
            continue

        #so sánh với số bí mật và đưa gợi ý
        if guess < secret_number:
            print("📉 Too low! Try a bigger number.")
        elif guess > secret_number:
            print("📈 Too high! Try a smaller number.")
        else:
            print(f"🎉 Correct! The secret number was {secret_number}.")
            print(f"👏 You guessed it in {attempts} attempts.")
            break

    except ValueError:
        #nếu nhapja sai
        print("⚠️ Please enter a valid integer (e.g., 42).")
