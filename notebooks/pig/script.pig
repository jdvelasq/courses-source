
-- crea la carpeta input in el HDFS
fs -mkdir tmp
fs -mkdir tmp/input

-- copia los archivos del sistema local al HDFS
fs -put input/ tmp/

-- carga de datos
lines = LOAD 'tmp/input/text*.txt' AS (line:CHARARRAY);

-- genera una tabla llamada words con una palabra por registro
words = FOREACH lines GENERATE FLATTEN(TOKENIZE(line)) AS word;

-- agrupa los registros que tienen la misma palabra
grouped = GROUP words BY word;

-- genera una variable que cuenta las ocurrencias por cada grupo
wordcount = FOREACH grouped GENERATE group, COUNT(words);

-- selecciona las primeras 15 palabras
s = LIMIT wordcount 15;

-- escribe el archivo de salida 
STORE s INTO 'tmp/output';

-- copia los archivos del HDFS al sistema local (genera la carpeta output en el directorio actual)
fs -get tmp/output/ .
