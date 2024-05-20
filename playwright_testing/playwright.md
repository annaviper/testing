```commandline
page.getByRole('heading', {name: 'Sign up'})
page.getByRole('checkbox', {name: 'Subscribe'})
page.getByRole('button', {name: /submit/i}).click()

page.getBytext('Welcome, John')

page.getByLabel('Password').fill('secret')

page.getByPlaceholder('name@example.com')

page.getByAltText('playwright logo')

page.getByTestId('directions')

expect(page.getByTitle('Issues count')).toHaveText('25 issues)
```