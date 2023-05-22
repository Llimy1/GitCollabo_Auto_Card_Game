import RPi.GPIO as GPIO

# 서보 모터 핀 설정
servo_pin = 18

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# PWM 설정
pwm = GPIO.PWM(servo_pin, 50)  # 주파수 50Hz (20ms 주기)
pwm.start(0)

# 듀티 사이클 변경 함수
def set_duty_cycle(duty_cycle):
    pwm.ChangeDutyCycle(duty_cycle)

try:
    while True:
        # 정시계방향 회전 (속도를 높이거나 줄이기 위해 듀티 사이클 값을 조정하세요.(2.5~7 사이) )
        set_duty_cycle(4.5)  # 4.5% 듀티 사이클로 설정 
        input("정방향 회전 중... 키를 누르세요.")
        
        # 정지
        set_duty_cycle(0)
        input("정지 중... 키를 누르세요.")
        
        # 역시계방향 회전 (소리를 높이거나 줄이기 위해 듀티 사이클 값을 조정하세요.(7~12.5 사이) )
        set_duty_cycle(9.5)  # 9.5% 듀티 사이클로 설정
        input("역방향 회전 중... 키를 누르세요.")

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
