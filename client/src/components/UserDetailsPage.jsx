import { useState, useEffect } from "react"
import { useLocation } from "react-router-dom/cjs/react-router-dom.min"
import AddPostForm from "./AddPostForm"

function UserDetailsPage() {
  const [posts, setPosts] = useState([])
  const { state: user } = useLocation()

  useEffect(() => {
    fetch(`/users/${user.id}/posts`)
      .then(res => res.json())
      .then(data => setPosts(data))
  }, [])

  function onAddPost(post) {
    setPosts([...posts, post])
  }

  return (
    <>
      <h1>{user.username}</h1>
      <p>Email: {user.email}</p>
      <p>Mobile No.: {user.mobile_number}</p>
      <h2>Posts</h2>
      <AddPostForm userId={user.id} onAddPost={onAddPost} />
      {posts.map((p, i) => <li key={i}>{p.title}</li>)}
    </>
  )
}

export default UserDetailsPage