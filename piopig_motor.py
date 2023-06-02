import pigpio
import time

# pigpio 인스턴스 생성
pi = pigpio.pi()

# 모터 핀 설정
MOTOR1_PIN = 17  # 모터1의 GPIO 핀 번호
MOTOR2_PIN = 27  # 모터2의 GPIO 핀 번호
MIN_PW = 1000    # 최소 펄스 폭
MAX_PW = 2000    # 최대 펄스 폭
MAX_COUNT = 20   # 최대 인원 수
TIME_DELAY = 1   # 모터 동작 지연 시간
ROTATE_TIME = 6  # 1초에 모터가 60도 회전한다고 생각하고 6초로 설정 (1초 각도 확인 후 재설정)

# 모터 시작 함수
def motor_start(motor_pin):
    pi.set_servo_pulsewidth(motor_pin, MAX_PW)

# 모터 정지 함수
def motor_stop(motor_pin):
    pi.set_servo_pulsewidth(motor_pin, MIN_PW)

# 모터 회전 설정 함수
def motor_rotate(motor_number, num_of_people, motor_pin, rotate_time):
    result = motor_number
    if motor_number != -1:
        motor_start(motor_pin)
        time.sleep(rotate_time)
        motor_stop(motor_pin)
        time.sleep(rotate_time)
        result += 1
    return result

# 프로그램의 메인 함수
def main():
    start = False
    motor1 = -1
    motor2 = -1
    confirm_start = False

    # 시작 여부 확인
    while not confirm_start:
        input_start = input("시작하시겠습니까? (yes/no): ").lower()
        if input_start == "yes":
            start = True
            confirm_start = True
        elif input_start == "no":
            print("시작하지 않습니다.")
            confirm_start = True
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

    if start:
        # 인원 수 설정
        while True:
            try:
                input_people = int(
                    input("몇 명의 인원 수가 이용하시겠습니까? (최대 {}명): ".format(MAX_COUNT))
                )
                if input_people < 1 or input_people > MAX_COUNT:
                    raise ValueError
                break
            except ValueError:
                print("잘못된 입력입니다. 1에서 {} 사이의 값을 입력해주세요.".format(MAX_COUNT))

        motor1 = 0
        motor2 = 0
        current_count = 1

        # 모터 동작
        while current_count < input_people:
            motor1 = motor_rotate(motor1, input_people, MOTOR1_PIN, ROTATE_TIME)
            motor2 = motor_rotate(motor2, input_people, MOTOR2_PIN, ROTATE_TIME)
            current_count += 1
        
        #동작 후 메세지 출력 및 모터 멈춤
        print("모든 모터의 동작이 종료되었습니다.")
        motor_stop(MOTOR1_PIN)
        motor_stop(MOTOR2_PIN)

    else:
        print("시작하지 않습니다.")

# 메인 함수 실행
if __name__ == "__main__":
    main()
