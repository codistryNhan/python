# use ** to create an argument for dictionary

def build_profile(first, last, **user_info):
  profile = {}
  profile['first_name'] = first
  profile['last_name'] = last
  for key,value in user_info.items():
    profile[key] = value
  return profile

profile = {}

profile = build_profile("nhan","nguyen",city='San Francisco', area_code='808')

print(profile)
