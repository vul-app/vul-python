aws_access_key_id = 'AKIAV6U7E6GGNKI4PMXR'
aws_secret_access_key = '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'

aws_access_key_id_2 = 'AKIAAAAAAAAAAAAAAAAA'
aws_secret_access_key_2 = '444444444444444444444444444444444444444'

def main():
    ###TESTING DATA###
    t_repo_url = "https://scm.platform.avalara.io/wanchun.li/docker-vulnerable-dvwa.git"
    t_project_cxm_info = dict()
    t_project_cxm_info["team_name"] = 'poc-team'  # default_values["CxXMLResults"]["Team"]
    t_project_cxm_info["project_id"] = '000'  # default_values["CxXMLResults"]["ProjectId"]
    t_project_cxm_info["project_name"] = 'proj-name'  # default_values["CxXMLResults"]["ProjectName"]
    ##################
    # repo_name = 'docker-vulnerable-dvwa'
    # bucket_name = 's-pipe-s3-irm-qa'
    # # download_source_zip(bucket_name, repo_name)
    # # download_and_unzip_zipped_file_from_s3(bucket_name, repo_name)
    # # # download_scan_result('docker-vulnerable-dvwa')
    # # s3_config_dict = load_iac_config(IAC_CONFIG_FILE)
    # # # get_cxm_credential()
    # # LOGGER.debug(s3_config_dict)
    #
    # handler_impl(t_repo_url)
    # LOGGER.debug('main done.')

    # iac_config_dict = load_iac_config()
    # msg = '{"repo":"https://scm.platform.avalara.io/dev-relations/secengine-testapplication.git", "type":"CD"}'
    print(t_repo_url, 'CI')


if __name__ == "__main__":
    main()