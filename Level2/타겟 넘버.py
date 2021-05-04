def solution(numbers, target):
    answer = 0

    def dfs(numbers,target,index):
        # answer이 solution 함수 안에서 정의되었으므로 global answer 을 하게 되면 에러가 발생 (전역변수로 선언된 answer이 없기 때문)
        # 이러한 경우 nonlocal 을 사용해야함
        nonlocal answer

        if index == len(numbers):
            if sum(numbers) == target:
                answer += 1
            return

        dfs(numbers,target,index+1)
        numbers[index] *= -1
        dfs(numbers,target,index+1)


    dfs(numbers,target,0)

    return answer
