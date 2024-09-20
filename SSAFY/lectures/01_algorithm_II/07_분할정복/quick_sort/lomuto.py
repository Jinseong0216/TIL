# lomuto
def lomuto_partition(left, right):
    idx = left - 1      # 모든 상황에 대해서 동일하게 코드를 작성
    pivot = arr[right]  # lomuto 방식은 for문으로 처리 할거라...
    '''
         left           right
          ↓               ↓
          3 2 4 6 9 1 8 7 5
        ↑                 ↑
        idx               p                         
    '''
    # right 번째 -> pivot, range(l, right) -> right-1
    for next in range(left, right):
        if arr[next] < pivot:
            idx += 1
            arr[idx], arr[next] = arr[next], arr[idx]
            '''   
                우연히, 첫 조사 대상부터 변경 대상이었으므로, 변경하지 않음.
                  next
                  ↓               
                  3 2 4 6 9 1 8 7 5
                  ↑               ↑
                  idx             p  
                조사를 거듭 하던 중...
                next의 값이 pivot보다 큰 경우가 발생 -> idx는 증가하지 않음.
                        next
                        ↓               
                  3 2 4 6 9 1 8 7 5
                      ↑           ↑
                      idx         p   
                다시... 조사를 거듭 하던 중...  
                next의 값이 pivot 보다 작은 경우 발생 -> idx랑 swap
                            next
                            ↓                
                  3 2 4 6 9 1 8 7 5
                        ↑         ↑
                        idx       p     
                            next
                            ↓                
                  3 2 4 1 9 6 8 7 5
                        ↑         ↑
                        idx       p                  
            '''
    '''
        for 문이 종료된 시점 기준,
        idx가 가리키고 있는 대상은, 무조건 pivot보다 작은 값
        idx보다 오른쪽은 무조건 pivot보다 큰 값이 있을 것이다.
              idx
              ↓                
        3 2 4 1 9 6 8 7 5
                        ↑
                        p
                idx
                ↓                
        3 2 4 1 5 6 8 7 9
                        ↑
                        p    
    '''
    arr[idx + 1], arr[right] = arr[right], arr[idx + 1]
    return idx + 1


def quick_sort(left, right):
    if left < right:
        pivot_idx = lomuto_partition(left, right)

        quick_sort(left, pivot_idx - 1)
        quick_sort(pivot_idx + 1, right)

arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(0, len(arr)-1)