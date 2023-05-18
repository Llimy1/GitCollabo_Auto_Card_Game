# 인원수 및 시작 데이터 ex) 4, 1 <- true 값이 1이므로 1을 송신

# 현재 각도에 따른 번호 ex) 1, 2, 3, 4

# Part1
# 모터 각도에 따라 (뽑은 카드 숫자 증가)

# 설정한 뽑은 카드 숫자에 도달하면 (stop)
# 각도에 따른 번호가 1이였으면 1증가 후 각도 모터에게 전송

# 인원수를 넘는 값이 들어오면 Part1 종료 신호 수신 (각도 모터, Rule)

# Part2 시작 데이터 수신
# 모터 각도에 따라 (뽑은 카드 숫자 증가)

# 설정한 뽑은 카드 숫자에 도달하면 (stop)
# 각도에 따른 번호가 1이였으면 1증가 후 각도 모터에게 전송

# 인원수를 넘는 값이 들어오면 Part2 종료 신호 수신 (각도 모터, Rule)

# 설정한 모든 Part가 끝나면 Rule과 각도 모터에게 종료 신호 수신


#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import rospy

# 모터 핀 설정
motor_pin = 18

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)

# 모터 핀 출력으로 설정
GPIO.setup(motor_pin, GPIO.OUT)

# 받은 인원수를 저장할 변수
people_number = msg

# 모터 제어 함수
def control_motor(speed, duration):
     # PWM 객체 생성: 모터 제어 주파수 100Hz로 설정
    pwm = GPIO.PWM(motor_pin, 100)
    # PWM 신호 출력 시작, 듀티 사이클 0%
    pwm.start(0)

    # 모터 속도 조절
    pwm.ChangeDutyCycle(speed)

    # 주어진 시간 동안 모터 작동
    time.sleep(duration)

    pwm.stop()  # PWM 정지
    GPIO.cleanup()  # GPIO 설정 초기화

# 인원수만큼 카드 분배 함수
# 1번 수행이 종료되면 Service 통신으로 종료 신호 보내고 다음 수신을 대기.
def people_count(people_number):


# 모터 제어
try:
    # 모터를 50% 속도로 2초간 작동
    control_motor(50, 2)
except KeyboardInterrupt:
    pass
