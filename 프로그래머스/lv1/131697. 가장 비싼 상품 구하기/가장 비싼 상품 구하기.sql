select price as max_price
from product
where price = (select max(price)
              from product)