# PSPD - Projeto de Pequisa 1 - Hadoop e Spark

## Execução do gerador de palavras aleatorias
```
$ python generator.py > input
# Generate a 700MB file with random words
```
## Preparação do HDFS
```
$ cd $SPARK_HOME
$ bin/hdfs namenode -format
$ bin/hadoop fs -mkdir -p /user/$USUARIO/
$ sbin/start-all.sh
```

## Subir o input para o HDFS
```
$ bin/hadoop -put input
```

## Execução da solução por Hadoop

```
$ bin/mapred streaming \
    -input input \
    -output output1 \
    -mapper mapper.py \
    -reducer reducer.py \
    -file reducer.py -file mapper.py \
    && \
    mapred streaming \
        -input output1 \
        -output output2 \
        -mapper mapper2.py \
        -reducer reducer2.py \
        -file reducer2.py -file mapper2.py
```

## Execução da solução por SPARK

### Inicie o Master e o Slaves
```
$ cd $SPARK_HOME
$ bin/start-master.sh
$ bin/start-worker.sh spark://MASTER_HOST:MASTER_PORT
```

### Submissão do Job
```
bin/spark-submit $PROJECT_PATH/sparkOtimized.py
```

** Altere a variavel hdfs_path nos arquivos spark*.py com o caminho do HDFS