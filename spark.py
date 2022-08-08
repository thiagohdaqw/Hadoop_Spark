from functools import partial
from pyspark import SparkContext, SparkConf


def word_startwith_filter(pair, start):
    """Funcao que filtra pelo comeco da palavra"""
    word, _ = pair
    return word.startswith(start)

def word_len_filter(pair, length): 
    """Funcao que filta pela quantidade de caracteres da palavra""" 
    word, _ = pair
    return len(word) == length

def total_count(dataset):
    """Retorna a quantidade total de palavras no dataset"""
    return dataset.map(lambda pair: pair[1]).sum() 

# Inicializa o Spark e passa o endereco do nó master
conf = SparkConf().setAppName('PSPD - P1').setMaster('spark://notebook:7077')
sc = SparkContext(conf=conf)
hdfs_path = "hdfs://notebook:9000/user/thiago"
# Abre o arquivo do HDFS
file = sc.textFile(hdfs_path + "/input")

# Mapeia cada palavra do arquivo em um par (Palavra, 1)
# Como pode ter mais de uma palavra por linha, utiliza-se o flatMap
words = file.flatMap(lambda l: ((w.lower(), 1) for w in l.split()))

# Agrupa as palavras e soma as quantidades
words_count = words.reduceByKey(lambda a, b: a + b)

# Avisa para salvar o conjunto de dados na memoria
words_count.cache()


# Datasets de palavras que comecam com S, P e R
s_words = words_count.filter(partial(word_startwith_filter, start='s'))
p_words = words_count.filter(partial(word_startwith_filter, start='p'))
r_words = words_count.filter(partial(word_startwith_filter, start='r'))

# Datasets de palavras com a quantidade de caracteres 6, 8 e 11
len_6_words = words_count.filter(partial(word_len_filter, length=6))
len_8_words = words_count.filter(partial(word_len_filter, length=8))
len_11_words = words_count.filter(partial(word_len_filter, length=11))   

# Salva as palavras em um arquivo no HDFS
words_count.saveAsTextFile(hdfs_path + "/spark-output/words")

# Cria e salva o sumario
sc.parallelize([
    ('TOTAL_WORDS', total_count(words_count)),
    ('TOTAL_S_WORDS', total_count(s_words)),
    ('TOTAL_P_WORDS', total_count(p_words)),
    ('TOTAL_R_WORDS', total_count(r_words)),
    ('TOTAL_6_WORDS', total_count(len_6_words)),
    ('TOTAL_8_WORDS', total_count(len_8_words)),
    ('TOTAL_11_WORDS', total_count(len_11_words)),
]).saveAsTextFile(hdfs_path + "/spark-output/result")