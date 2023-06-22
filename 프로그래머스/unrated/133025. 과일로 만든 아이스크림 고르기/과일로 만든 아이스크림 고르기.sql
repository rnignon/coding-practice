select i.flavor
from first_half as f, icecream_info as i
where f.flavor = i.flavor and
		f.total_order >= 3000 and
        i.ingredient_type = 'fruit_based'