DROP TABLE empenhos_detalhados;
DROP TABLE empenhos_detalhados_por_ano; 

CREATE TABLE `empenhos_detalhados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero` varchar(10) NOT NULL,
  `tipo` varchar(2) NOT NULL,
  `data` date NOT NULL,
  `ano` varchar(4) NOT NULL,
  `descricao` mediumtext NOT NULL,
  `natureza` varchar(20) NOT NULL,
  `nome_natureza` varchar(200) NOT NULL,
  `dotacao` double NOT NULL,
  `alteracao_dotacao` double NOT NULL,
  `dotacao_atual` double NOT NULL,
  `valor_anulado` double NOT NULL,
  `valor_empenhado` double NOT NULL,
  `valor_liquidado` varchar(20) NOT NULL,
  `valor_pago` double NOT NULL,
  `empenhado_ate_hoje` double NOT NULL,
  `liquidado_ate_hoje` double NOT NULL,
  `pago_ate_hoje` double NOT NULL, 
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;




