import aws_cdk as core
import aws_cdk.assertions as assertions

from analytiikka_tie.analytiikka_tie_stack import AnalytiikkaTieStack

# example tests. To run these tests, uncomment this file along with the example
# resource in analytiikka_tie/analytiikka_tie_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AnalytiikkaTieStack(app, "analytiikka-tie")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
