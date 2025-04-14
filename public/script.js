document.getElementById('fetchData').addEventListener('click', async () => {
    const response = await fetch('/api/hello');
    const data = await response.json();
    document.getElementById('output').textContent = data.message;
  });