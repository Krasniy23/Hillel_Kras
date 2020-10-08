def fake_string(fake_string1, replace_fake_string, new_fake_string):
    result = fake_string1.replace(replace_fake_string, new_fake_string)
    return result


print(fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel'))

