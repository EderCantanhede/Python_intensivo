frameworks = {
    'frame1': 'flutter', 'frame2': 'node.js', 'frame3': 'angular',
    'frame4': 'vue'
}
for name in frameworks.values():
    print(name.title())
frameworks['frame5'] = 'react'
for name1 in frameworks.values():
    print(name1.title())
