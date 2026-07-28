def create_post(form, author):
    post = form.save(commit=False)
    post.author = author
    post.save()
    return post
    