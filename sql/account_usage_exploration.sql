use role accountadmin;
use warehouse compute_wh;
use database snowflake;
use schema account_usage;

show views in schema account_usage;

select *
from warehouse_metering_history;

select *
from query_history;

select *
from warehouse_load_history;

--warehouse metering history : how much compute was used
select
    start_time,
    end_time,
    warehouse_name,
    credits_used
from warehouse_metering_history
order by start_time desc
limit 10;

--query history : what caused the compute
select
    query_id,
    warehouse_name,
    user_name,
    total_elapsed_time,
    execution_time,
    query_text
from query_history
order by total_elapsed_time desc
limit 10;

--warehouse load history : was compute actually needed
select
    warehouse_name,
    start_time,
    avg_running,
    avg_queued_load,
    avg_queued_provisioning
from warehouse_load_history
order by start_time desc
limit 10;