import jenkins
JOB_NAME = 'trunk/flamingo-regression/flamingo-bm-regression-task'


server = jenkins.Jenkins('http://ci.int.zone/jenkins', username='rkoryakin', password='Fylhjvtlf7?')

#get last 42 builds
builds = server.get_job_info(JOB_NAME)['builds']
last_builds = builds

data = []
last_builds = [server.get_build_info(JOB_NAME, build_data['number']) for build_data in last_builds]

for build_data in last_builds:
    current_info = {
        "duration": build_data['duration'],
        "displayName": build_data['displayName'].split("---")[0],
        "tests_build": build_data['displayName'].split("---")[1],
        "number": build_data['number']
    }

    was_such = False
    for i in xrange(len(data)):
        saved_build = data[i]

        if saved_build["displayName"] == current_info["displayName"]:
            was_such = True
            if current_info["number"] > saved_build["number"]:
                data[i] = current_info
            break

    if not was_such:
        data.append(current_info)


res = sorted(data, key=lambda x: x["duration"], reverse=True)
for build_data in res:
    [job_name, build_number] = build_data["displayName"], build_data["number"]
    duration = build_data["duration"]
    tbuild = build_data["tests_build"]
    print "job: '%s', build: '%s', tbuild: '%s', duration : '%s'" % (job_name, build_number, tbuild, duration / 3600000.0)


count_lower = 0
total_hours_lower = 0
total_stacks_lower = 0
for build_data in res:
    duration_in_hours = build_data["duration"] / 3600000.0
    if duration_in_hours < 8:
        total_hours_lower += duration_in_hours
        total_stacks_lower += 1
        count_lower += 8 - duration_in_hours

print "hours_lower: '%s', total_hours_lower: '%s', stacks_lower: '%s'" % (count_lower, total_hours_lower, total_stacks_lower)

count_upper = 0
total_hours_upper = 0
total_stacks_upper = 0
for build_data in res:
    duration_in_hours = build_data["duration"] / 3600000.0
    if duration_in_hours > 8:
        count_upper += duration_in_hours - 8
        total_hours_upper += duration_in_hours
        total_stacks_upper += 1

print "hours_upper: '%s', total_hours_upper: '%s', stacks_upper: '%s'" % (count_upper, total_hours_upper, total_stacks_upper)

total_hours = sum([x["duration"] / 3600000.0 for x in res])

print "total_hours: %s" % total_hours