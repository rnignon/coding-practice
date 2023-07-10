-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, sum(b.price) as TOTAL_SALES
from USED_GOODS_BOARD as b, USED_GOODS_USER as u
where b.writer_id = u.user_id and b.status = 'DONE'
group by b.writer_id
having total_sales >= 700000
order by total_sales
