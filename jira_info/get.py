from jira import JIRA
import pickle
import os

def vlm_get_comments(issue_id):
    import jira.client
    options = {'server': 'http://vlm.lge.com/issue'}
    # options = {str('server'): str(jira_url)}
    jira = jira.client.JIRA(options, basic_auth = ("hoach.dang", "Hanoimuathu21$"))
    issue = jira.issue(issue_id)
    comments =  issue.fields.comment.comments

    for comment in comments:
        print("Comment text : \n",comment.body)
        # print("Comment author : ",comment.author.displayName)
        # print("Comment time : ",comment.created)

        fn = issue_id + ".pickle"
        a_file = open(fn , "wb")
        pickle.dump(comment, a_file)
        a_file.close()
        os.chmod(fn , 0o777)

def vlm_get_subtask(parent_issue):
    import jira.client
    options = {'server': 'http://vlm.lge.com/issue'}
    # options = {str('server'): str(jira_url)}
    jira = jira.client.JIRA(options, basic_auth = ("hoach.dang", "Hanoimuathu21$"))
    issue = jira.issue(parent_issue)

    print(issue.fields.subtasks) 

    fn = parent_issue + ".pickle"
    a_file = open(fn , "wb")
    pickle.dump(issue.fields.subtasks, a_file)
    a_file.close()
    os.chmod(fn , 0o777)


if (__name__ == "__main__"):
    vlm_get_comments('GENXII-1310')
    vlm_get_subtask('GENXII-767')

    #os.system('chmod 777 -R ./GEN*')
#a_file = open("data.json", "rb")
#output = a_file.read()
#print(output)
#a_file.close()
