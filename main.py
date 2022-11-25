import logging
import time

def get_log(log_name):
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG) #디버그 인포 워닝 에러 크리티컬
    
    if len(logger.handlers) > 0:
        return logger

    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s") #시간, 로그이름, 로그레벨, 로그메세지

    stream_handler = logging.StreamHandler() #콘솔 표시
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler('./log.log', encoding='utf-8')  # 로그 파일 생성(인코딩, utf-8)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

log = get_log('log_1')
log.info('booting')

log_2 = get_log("log_2")
log_2.info("off")
log.info('booting')

#--------------------------------------

cnt = 0
try:
    while True:
        cnt += 1
        time.sleep(1)
        print("!!!!!!!")
        if cnt > 10:
            raise IndentationError # 에러를 강제로 발생시켜 반복문 탈출

except KeyboardInterrupt as e:
    print(e)
except IndentationError:
    print('10을 넘음')

#---------------------------------------



