import { useState } from "react"

const initialPost = {
  title: "",
  body: ""
}

function AddPostForm({ userId, onAddPost }) {
  const [post, setPost] = useState(initialPost)

  function handleChange(e) {
    setPost({
      ...post,
      [e.target.name]: e.target.value
    })
  }

  function handleSubmit(e) {
    e.preventDefault()
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accepts': 'application/json'
      },
      body: JSON.stringify(post)
    }

    fetch(`/users/${userId}/posts`, options)
      .then(res => res.json())
      .then(data => {
        onAddPost(data)
        setPost(initialPost)
      })
  }

  return (
    <form onSubmit={handleSubmit}>
      <input name="title" onChange={handleChange} type="text" placeholder="title" value={post.title} /><br />
      <input name="body" onChange={handleChange} type="text" placeholder="body" value={post.body} /><br />
      <input type="submit" /><br />
    </form>
  )
}

export default AddPostForm