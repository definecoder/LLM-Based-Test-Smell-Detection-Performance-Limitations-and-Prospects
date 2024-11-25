import os

from groq import Groq
from smells import getAllSmellsInASingleString
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(        
    api_key=groq_api_key,
)

all_smells = getAllSmellsInASingleString()

def detectSmellWithGroq(test_code: str, production_code: str) -> list[str]:

    chat_completion = client.chat.completions.create(    
        messages=[
            {
                "role": "system",
                "content": "You are an expert in detecting test smells. You will be given a test code block and a production code block. You have to identify which smells the test code contains. The test block may contain multiple smells, single smell or no smells at all. Here is the list of test smells: " + all_smells
            },
            {
                "role": "user",
                "content": "Here is the test code block:" + test_code + "Here is the production code block:" + production_code + "Tell the name of the test smell(s) the test code block contains",
            }
        ],
        model="mixtral-8x7b-32768",
    )

    # print(chat_completion.choices[0].message.content)
    
    return chat_completion.choices[0].message.content
    

if __name__ == "__main__":
    test_code = """
    @Test
    public void realCase() {
        Point p34 = new Point("34", 556506.667, 172513.91, 620.34, true);
        Point p45 = new Point("45", 556495.16, 172493.912, 623.37, true);
        Point p47 = new Point("47", 556612.21, 172489.274, 0.0, true);
        Abriss a = new Abriss(p34, false);
        a.removeDAO(CalculationsDataSource.getInstance());
        a.getMeasures().add(new Measure(p45, 0.0, 91.6892, 23.277, 1.63));
        a.getMeasures().add(new Measure(p47, 281.3521, 100.0471, 108.384, 1.63));

        try {
            a.compute();
        } catch (CalculationException e) {
            Assert.fail(e.getMessage());
        }

        // test intermediate values with point 45
        Assert.assertEquals("233.2405",
            this.df4.format(a.getResults().get(0).getUnknownOrientation()));
        Assert.assertEquals("233.2435",
            this.df4.format(a.getResults().get(0).getOrientedDirection()));
        Assert.assertEquals("-0.1", this.df1.format(
            a.getResults().get(0).getErrTrans()));

        // test intermediate values with point 47
        Assert.assertEquals("233.2466",
            this.df4.format(a.getResults().get(1).getUnknownOrientation()));
        Assert.assertEquals("114.5956",
            this.df4.format(a.getResults().get(1).getOrientedDirection()));
        Assert.assertEquals("0.5", this.df1.format(
            a.getResults().get(1).getErrTrans()));

        // test final results
        Assert.assertEquals("233.2435", this.df4.format(a.getMean()));
        Assert.assertEquals("43", this.df0.format(a.getMSE()));
        Assert.assertEquals("30", this.df0.format(a.getMeanErrComp()));
    }
    """
    production_code = "not available"

    res = detectSmellWithGroq(test_code, production_code)
    
    print(res)
    print(type(res))