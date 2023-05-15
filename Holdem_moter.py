# 인원수와 시작 데이터를 입력 받을 Subscriber 생성
# 종료 신호 보낼 Publisher 생성

# 현재 각도에 몇번 인원인지 데이터를 수신
# 각도 모터에게 다음 인원의 각도를 돌릴 수 있는 값 전송
# ros data 출력 숫자를 1씩 증가시켜 일정 카드가 모두 배분되면 1회 종료
# 각도를 돌린 후 완료 데이터 수신
# 다시 횟수 시작 (설정된 인원수를 넘는 수신이 올 경우 분배 종료)
# 인원수 설정 후 인원수에 맞는 횟수를 돌면 1번 cycle 종료



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
