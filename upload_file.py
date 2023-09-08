from ftplib import FTP
import os
import mqtt_pub

def run():
    ftp = FTP('192.168.0.15')
    ftp.login(user='scapture', passwd='1234')
    
    # 전송할 파일 디렉토리
    local_file_directory = 'output/'
    file_list = os.listdir(local_file_directory)
    
    for filename in file_list:
        local_file_path = os.path.join(local_file_directory,filename)
        with open(local_file_path, 'rb') as local_file:
            # 전송 받을 서버의 디렉토리 주소
            remote_path = f'/Users/gesal03/Documents/Hansung/Scapture/ftp/output/{filename}'
            ftp.storbinary(f'STOR {remote_path}', local_file)  
    
    print("complete Upload")
    mqtt_pub.run()
    ftp.quit()