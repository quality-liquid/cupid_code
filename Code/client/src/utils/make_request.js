import { parse } from "cookie";

export async function makeRequest(uri, method = "get", body = {}) {
  const parsedCookie = parse(document.cookie)
  const options = {
    method,
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-CSRFToken": parsedCookie.csrftoken
    },
    credentials: "include",
  }
  const methodLower = method.toLowerCase();
  if (methodLower !== 'get' && Object.keys(body || {}).length > 0) {
    options.body = JSON.stringify(body)
  }

  const result = await fetch(uri, options);
  if (result.status === 204) return null;
  const text = await result.text();
  if (!text) return null;
  try {
    return JSON.parse(text);
  } catch (e) {
    return text;
  }
}

export async function makeRequestRaw(uri, method = "get", body = {}) {
  const parsedCookie = parse(document.cookie)
  const options = {
    method,
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-CSRFToken": parsedCookie.csrftoken
    },
    credentials: "include",
  }
  const methodLower = method.toLowerCase();
  if (methodLower !== 'get' && Object.keys(body || {}).length > 0) {
    options.body = JSON.stringify(body)
  }

  const result = await fetch(uri, options);
  return result;
}

export async function logoutRequest() {
    const parsedCookie = parse(document.cookie)
    const options = {
        'method':'get',
        headers: {
          "X-CSRFToken": parsedCookie.csrftoken
        },
        credentials: "include",
    }
    await fetch('/logout/', options);
}
