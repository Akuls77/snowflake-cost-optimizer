create database cost_optimization_db;
create schema metrics;

create or replace table cost_metrics_daily as 
select
    warehouse_name,
    DATE_TRUNC('day',start_time) as usage_date,
    SUM(credits_used) as total_credits_used
from snowflake.account_usage.warehouse_metering_history
group by
    warehouse_name,
    usage_date
order by usage_date desc;

select * from cost_metrics_daily;