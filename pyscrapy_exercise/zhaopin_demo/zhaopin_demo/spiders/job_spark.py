'''通过spark-Streaming,
对实时数据做简单处理后保存到hdfs上.'''
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
if __name__ == '__main__':
    sc = SparkContext(appName='job_demo')
    ssc = StreamingContext(sc,10)
    kssc = KafkaUtils.createDirectStream(ssc,['test'],{'metadata.broker.list','python2:9092'})
    lines = kssc.map(lambda x:x[1])
    lines.saveAsTextFiles('/user/hadoop/job_data/')
    ssc.start()
