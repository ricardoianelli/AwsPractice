using System;
using Amazon.CDK;
using Amazon.CDK.AWS.S3;
using Constructs;
using S3Bucket = Amazon.CDK.AWS.S3.Bucket;

namespace Bucket
{
    public class BucketStack : Stack
    {
        internal BucketStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            String timeNowString = DateTime.Now.ToString("yyyy-MM-dd-HH-mm-ss");
            BucketProps bucketProps = new BucketProps
            {
                BucketName = $"bucket-{timeNowString}",
                Versioned = true,
                RemovalPolicy = RemovalPolicy.DESTROY,
                AutoDeleteObjects = true
            };
            
            new S3Bucket(this, "MyBucket", bucketProps);
        }
    }
}
