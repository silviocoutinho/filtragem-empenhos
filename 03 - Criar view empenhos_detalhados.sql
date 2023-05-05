CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `empenhos_detalhados_por_ano` AS
select
    `empenhos_detalhados`.`ano` AS `ano`,
    count(`empenhos_detalhados`.`ano`) AS `quantidade`
from
    `empenhos_detalhados`
group by
    `empenhos_detalhados`.`ano`
order by
    `empenhos_detalhados`.`ano` desc