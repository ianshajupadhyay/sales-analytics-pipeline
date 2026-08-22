with date_spine as (

    select
        generate_series(
            '2016-01-01'::date,
            '2018-12-31'::date,
            interval '1 day'
        )::date as date_day

)

select
    date_day,

    extract(year from date_day)::int as year,

    extract(quarter from date_day)::int as quarter,

    extract(month from date_day)::int as month,

    to_char(date_day, 'Month') as month_name,

    extract(week from date_day)::int as week_of_year,

    extract(day from date_day)::int as day_of_month,

    extract(isodow from date_day)::int as day_of_week,

    to_char(date_day, 'Day') as day_name,

    case
        when extract(isodow from date_day) in (6, 7)
            then true
        else false
    end as is_weekend

from date_spine