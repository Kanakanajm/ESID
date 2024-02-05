import React, { useContext } from 'react'
import { AuthContext, AuthProvider, IAuthContext, TAuthConfig, TRefreshTokenExpiredEvent } from "react-oauth2-code-pkce"
import { TTokenData } from 'react-oauth2-code-pkce/dist/Types'

const authConfig: TAuthConfig = {
  clientId: process.env.OAUTH_CLIENT_ID!, // eslint-disable-line @typescript-eslint/no-non-null-assertion
  authorizationEndpoint: process.env.OAUTH_IDP_AUTH_ENDPOINT!, // eslint-disable-line @typescript-eslint/no-non-null-assertion
  tokenEndpoint: process.env.OAUTH_IDP_TOKEN_ENDPOINT!, // eslint-disable-line @typescript-eslint/no-non-null-assertion
  redirectUri: process.env.OAUTH_REDIRECT_URI!, // eslint-disable-line @typescript-eslint/no-non-null-assertion
  scope: 'openid read:admin-messages',
  decodeToken: true,
  onRefreshTokenExpire: (event: TRefreshTokenExpiredEvent) =>
    window.confirm('Session expired. Refresh page to continue using the site?') && event.login(),
  extraAuthParameters: {
    "audience": process.env.OAUTH_API_AUDIENCE! // eslint-disable-line @typescript-eslint/no-non-null-assertion
  }
}


function TokenBlock({token}: {token: string}) {
    return (
        <div style={{width: "100%", overflowX: "scroll"}}>
            <pre style={{whiteSpace: "pre-wrap"}}>{token}</pre>
        </div>
    )
}

function TokenDataBlock({data}: {data: TTokenData}) {
    return (
        <pre>{JSON.stringify(data, null, 2)}</pre>
    )
}

function AccessTokenInfo() {
    const {token, tokenData} = useContext<IAuthContext>(AuthContext)

    return (
    <div>
        <h3>Access Token Info</h3>
        <h5>Access Token:</h5>
        <TokenBlock token={token} />
        <h5>Access Token Data:</h5>
        {
            tokenData && <TokenDataBlock data={tokenData} />
        }
    </div>
    )
}

function UserInfo() {
    const {idToken, idTokenData} = useContext<IAuthContext>(AuthContext)

    return (
    <div>
        <h3>User Info</h3>
        <h5>Id Token:</h5>
        {
            idToken && <TokenBlock token={idToken} />
        }
        <h5>User Information from JWT:</h5>
        {
            idTokenData && <TokenDataBlock data={idTokenData} />
        }
    </div>
    )
}

function AccountPanel() {
    const {login, logOut, token, idToken} = useContext<IAuthContext>(AuthContext)
    const isAuthenticated = idToken !== undefined

    return (
        <div style={{display: "flex", alignItems: "center", gap: "10px"}}>
            {isAuthenticated ? (
                <>
                <button onClick={() => getMessage('/protected/private', token)}>Get Protected Message</button>
                <button onClick={() => getMessage('/protected/private-scoped', token)}>Get Admin Meesage</button>
                <button onClick={() => logOut()}>Logout</button>
                </>
            ) : (
            <button onClick={() => login()}>Login</button>
            )}
        </div>
    )
}

function getMessage(path: string, token: string) {
    // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
    fetch(process.env.API_URL! + path, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    }).then(response => {
        if (response.ok) {
            response.text().then((txt => {
                alert(txt)
            }))
            .catch(error => console.error(error))
        } else {
            console.error(response)
            alert(`Get Message Request Failed [HTTP ${response.status}]!, please check console for verbose output`)
        }
    }).catch(error => console.error(error))
}

function SecureApp() {
    return (
    <AuthProvider authConfig={authConfig}>
        <AccessTokenInfo />
        <hr />
        <UserInfo/>
        <hr />
        <AccountPanel />
    </AuthProvider>
    )
}

export default SecureApp