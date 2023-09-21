card_counts, target_num = map(int, input().split())
card_nums = list(map(int, input().split()))
answer = 0
for i in range(card_counts):
    for j in range(i+1, card_counts):
        for k in range(j+1, card_counts):
            cards_sum = card_nums[i] + card_nums[j] + card_nums[k]
            if cards_sum > target_num:
                continue
            else:
                answer = max(answer, cards_sum)
print(answer)