import time
import subprocess

def run_shell(cmd):
    result = b''
    stoptime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()+1))
    print('stoptime', stoptime)  
    p = subprocess.Popen(cmd,
                         bufsize=1,
                         stdout=subprocess.PIPE,
#                         stderr=subprocess.PIPE,
                         shell=True)
    for b in iter(p.stdout.readline, b''):
    #for b in p.stdout:
        if not b:
            break
        result += b
        #当前时间
        curtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print('curtime', curtime)
        if curtime>=stoptime:
            print('tiao chu')
            break
            #终止子进程
            p.terminate()
            #等待子进程终止后跳出while循环
            if subprocess.Popen.poll(p) is not None:
                print('进程终止～～～')
                break
            else:
                print(u'等待subprocess子进程终止。')
    print(u'完成----------------------------')
    print(result.decode('utf-8'))
    
    
#cmd = "ls /home/pi"
cmd = "ping www.baidu.com"
#cmd = "vim /home/test.txt" # 不支持这种命令，会卡死～～
run_shell(cmd)
    