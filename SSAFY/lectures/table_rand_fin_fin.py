import csv, random, copy
from datetime import datetime

t = datetime.today().strftime("%Y-%m-%d")

def files(fname):
    table_lst=[]
    try:
        f = open(f"{fname}.csv", "r", encoding="UTF-8")
    except(NameError, FileNotFoundError):
        print(f"{fname}.csv 파일이 없습니다.")
        return False
    else:
        try:
            reader = csv.reader(f)
        except UnboundLocalError:
            print("파일명을 다시 입력해주세요")
        else:
            try:
                for row in reader:
                    table_lst.extend(row)
            except UnicodeDecodeError:
                f.close()
                try:
                    f = open(f"{fname}.csv", "r", encoding="EUC-KR")
                except(NameError, FileNotFoundError):
                    print(f"{fname}.csv 파일이 없습니다.")
                    return False
                else:
                    try:
                        reader = csv.reader(f)
                    except UnboundLocalError:
                        print("파일명을 다시 입력해주세요")
                    else:
                        try:
                            for row in reader:
                                table_lst.extend(row)
                        except UnicodeDecodeError:
                            f.close()
                            try:
                                f = open(f"{fname}.csv", "r", encoding="cp949")
                            except(NameError, FileNotFoundError):
                                print(f"{fname}.csv 파일이 없습니다.")
                                return False
                            else:
                                try:
                                    reader = csv.reader(f)
                                except UnboundLocalError:
                                    print("파일명을 다시 입력해주세요")
                                else:
                                    try:
                                        for row in reader:
                                            table_lst.extend(row)
                                    except UnicodeDecodeError:
                                        return False
                                    else:
                                        f.close()
                                        return table_lst
                        else: 
                            f.close()
                            return table_lst
            else:    
                f.close()
                return table_lst

def tab(table_lst):
    random.shuffle(table_lst)
    table_lst = list(set(list(set(table_lst))))

    f = open(f"{t}.csv", "w", newline="", encoding="UTF-8")
    writer = csv.writer(f)

    print()
    print('-'*20+'칠판'+'-'*20)
    print()
    for i in range(4):
        row=[]
        for j in range(6):
            if j==3:print(end = '\t')
            print(table_lst[j+6*i], end=' ')
            row.append(table_lst[j+6*i])
            if j==5:
                writer.writerow(row)
        print()
    print()
    print()

    f.close()

def tabexam(new_table_lst):
    table_lst = copy.deepcopy(new_table_lst)
    while(1):
        random.shuffle(new_table_lst)
        random.shuffle(new_table_lst)
        random.shuffle(new_table_lst)
        cnt=0
        for i in range(len(new_table_lst)):
            if table_lst[i]==new_table_lst[i]:
                cnt+=1
                break
        if cnt==0:
            break

    
    f = open(f"{t}.csv", "w", newline="", encoding="UTF-8")
    writer = csv.writer(f)

    print()
    print('-'*20+'칠판'+'-'*20)
    print()
    for i in range(4):
        row=[]
        for j in range(6):
            if j==3:print(end = '\t')
            print(new_table_lst[j+6*i], end=' ')
            row.append(new_table_lst[j+6*i])
            if j==5:
                writer.writerow(row)
        print()
    print()
    print()

    f.close()

def readtab(table_lst):
    print()
    print('-'*20+'칠판'+'-'*20)
    print()
    for i in range(4):
        row=[]
        for j in range(6):
            if j==3:print(end = '\t')
            print(table_lst[j+6*i], end=' ')
            row.append(table_lst[j+6*i])
        print()
    print()
    print()


if __name__ == '__main__':
    fname = input("이전 데이터 파일명을 입력해주세요. (YYYY-MM-DD) : ")
    read=files(fname)
    if read:    
        while(1):
            try:
                w=int(input("\n1. 현재 자리 보기 2. 랜덤 자리배정 후 저장/종료 (종료 :0) : "))
            except:
                print("숫자만 입력할 수 있습니다.")
                continue
            else:
                if w==0:
                    print('프로그램을 종료합니다.\n')
                    break
                elif w==1:
                    readtab(read)
                elif w==2:
                    try:
                        h=int(input("\n1. 자리 지속 허용 2. 자리 지속 불가(시험 배치) (종료 :0) : "))
                    except:
                        print("숫자만 입력할 수 있습니다.")
                    else:
                        if h==0:
                            print('프로그램을 종료합니다.\n')
                            break
                        elif h==1:
                            tab(read)
                            break
                        elif h==2:
                            tabexam(read)
                            break
                        else:
                            print("유효한 숫자를 입력해주세요")
                        break
                else:
                    print("유효한 숫자를 입력해주세요")
