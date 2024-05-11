from generics.entity import recursively_calculate_total_exp_at_level, \
    non_recursively_calculate_total_exp_at_level, calculate_level_from_total_exp

print(recursively_calculate_total_exp_at_level(1))
print(recursively_calculate_total_exp_at_level(2))
print(recursively_calculate_total_exp_at_level(3))
print(recursively_calculate_total_exp_at_level(4))
print(recursively_calculate_total_exp_at_level(5))
print('\n')
print(non_recursively_calculate_total_exp_at_level(1))
print(non_recursively_calculate_total_exp_at_level(2))
print(non_recursively_calculate_total_exp_at_level(3))
print(non_recursively_calculate_total_exp_at_level(4))
print(non_recursively_calculate_total_exp_at_level(5))
print('\n')
print(recursively_calculate_total_exp_at_level(12))
print(recursively_calculate_total_exp_at_level(13))
print('\n')
calculate_level_from_total_exp(12.5)
calculate_level_from_total_exp(37.5)
calculate_level_from_total_exp(75)


