from functools import partial
from pyspark import SparkContext, SparkConf


# Inicializa o Spark e passa o endereco do nó master
conf = SparkConf().setAppName('PSPD - P1').setMaster('spark://gpu1.esw:7077')
sc = SparkContext(conf=conf)
hdfs_path = "hdfs://gpu1:7777/user/a190020377"
# Abre o arquivo do HDFS
file = sc.textFile(hdfs_path + "/input")

# Mapeia cada palavra do arquivo em um par (Palavra, 1)
# Como pode ter mais de uma palavra por linha, utiliza-se o flatMap
words = file.flatMap(lambda l: ((w.lower(), 1) for w in l.split()))

# Agrupa as palavras e soma as quantidades
words_count = words.reduceByKey(lambda a, b: a + b)

# Avisa para salvar o conjunto de dados na memoria
words_count.cache()

infos = {
    'all': 'TOTAL_WORDS',
    's': 'TOTAL_S_WORDS',
    'p': 'TOTAL_P_WORDS',
    'r': 'TOTAL_R_WORDS',
    '6': 'TOTAL_6_WORDS',
    '8': 'TOTAL_8_WORDS',
    '11': 'TOTAL_11_WORDS',
}

def find_infos(pair):
    word, count = pair
    len_word = len(word)
    initial_letter = word[0]
    result = [(infos['all'], count)]

    if initial_letter in 'spr':
        result.append((infos[initial_letter], count))
    if len_word in [6, 8, 11]:
        result.append((infos[str(len_word)], count))
    return result

# Salva as palavras em um arquivo no HDFS
words_count.saveAsTextFile(hdfs_path + "/spark-output/words")

# Itera sobre o dataset
summary = words_count.flatMap(find_infos).reduceByKey(lambda a, b: a+b)

# Salva o sumario
summary.saveAsTextFile(hdfs_path + "/spark-output/result")