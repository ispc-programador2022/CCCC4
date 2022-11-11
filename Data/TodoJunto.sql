/*
-- Query: SELECT ranking.Pais, ranking.Puntos, equipos.Equipos, poblacion.Pais, Avg(reventa.CAT1) AS PromedioDeCAT1, poblacion.Poblacion, Sum(equipos.Goles) AS SumaDeGoles, ranking.Puntos
FROM ((reventa LEFT JOIN ranking ON reventa.Pais1 = ranking.Pais) LEFT JOIN equipos ON reventa.Pais1 = equipos.Equipos) LEFT JOIN poblacion ON reventa.Pais1 = poblacion.Pais
GROUP BY ranking.Pais, ranking.Puntos, equipos.Equipos, poblacion.Pais, poblacion.Poblacion, ranking.Puntos
LIMIT 0, 1000

-- Date: 2022-11-10 23:43
*/
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Catar,1440,Catar,Catar,645.0000,2930524,366,1440);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Senegal,1584,Senegal,Senegal,350.0000,17196308,62,1584);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Inglaterra,1728,Inglaterra,Inglaterra,250.0000,67081000,222,1728);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Estados Unidos,1627,Estados Unidos,Estados Unidos,330.0000,332183000,94,1627);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Francia,1760,Francia,Francia,245.0000,67842582,368,1760);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Dinamarca,1667,Dinamarca,Dinamarca,225.0000,5873420,139,1667);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (México,1645,México,México,400.0000,130262220,100,1645);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Argentina,1774,Argentina,Argentina,435.0000,45808747,326,1774);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Bélgica,1817,Bélgica,Bélgica,215.0000,11631136,498,1817);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (España,1715,España,España,285.0000,47432805,160,1715);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Alemania,1650,NULL,Alemania,225.0000,83237124,NULL,1650);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Marruecos,1564,Marruecos,Marruecos,250.0000,36313000,75,1564);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Suiza,1636,Suiza,Suiza,200.0000,8736510,143,1636);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Uruguay,1639,Uruguay,Uruguay,270.0000,3485152,93,1639);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Portugal,1677,Portugal,Portugal,262.5000,10352042,434,1677);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Brasil,1841,Brasil,Brasil,385.0000,213993441,288,1841);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Gales,1570,Gales,Gales,315.0000,2278829,184,1570);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Países Bajos,1695,Países Bajos,Países Bajos,310.0000,17590672,202,1695);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Túnez,1508,Túnez,Túnez,420.0000,11935764,206,1508);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Polonia,1549,Polonia,Polonia,370.0000,37654247,334,1549);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Japón,1560,Japón,Japón,322.5000,125681593,182,1560);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Croacia,1646,Croacia,Croacia,320.0000,3879074,260,1646);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Camerún,1471,Camerún,Camerún,335.5000,27224262,78,1471);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Corea del Sur,1530,Corea del Sur,Corea del Sur,352.5000,51736000,218,1530);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Irán,1565,Irán,Irán,225.0000,84841000,143,1565);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Ecuador,1464,Ecuador,Ecuador,225.0000,17888474,67,1464);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Australia,1489,Australia,Australia,270.0000,25767000,73,1489);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Arabia Saudita,1438,Arabia Saudita,Arabia Saudita,200.0000,35340680,96,1438);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Canadá,1475,Canadá,Canadá,320.0000,38929902,113,1475);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Costa Rica,1504,Costa Rica,Costa Rica,180.0000,5180000,115,1504);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Ghana,1393,Ghana,Ghana,420.0000,31394000,102,1393);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (Serbia,1564,Serbia,Serbia,420.0000,6797105,112,1564);
INSERT INTO `` (`Pais`,`Puntos`,`Equipos`,`Pais`,`PromedioDeCAT1`,`Poblacion`,`SumaDeGoles`,`Puntos`) VALUES (NULL,NULL,NULL,NULL,415.7143,NULL,NULL,NULL);
