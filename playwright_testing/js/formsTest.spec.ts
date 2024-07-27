import {test} from "@playwright/test"

// runs before each suite
test.beforeEach( async({page}) => {
    await page.goto('http://localhost:4200/')
})

test.describe('Forms', () => {
    // runs before each test in this suite
    test.beforeEach(async({page}) => {
        await page.getByText('Forms').click()
        await page.getByText('Form Layout').click()
    })

    // .locator() html tags
    test('locator syntax rules', async ({page}) => {
        // tag
        await page.locator('input').first().click()

        // ID
        page.locator('#inputEmail1')

        // class
        page.locator('.shape-rectangle')
        // full class
        page.locator('[class="write here the whole class"]')

        // attribute
        page.locator('[placeholder="Email"]')

        // combine different selectors
        page.locator('input[placeholder="Email"][nbinput]')

        // text exact match
        page.locator(':text-is("Using the Grid")')
        // partial text
        page.locator(':text("Using")')

        // XPATH (not recommended)
        page.locator('//*[@id="inputEmail1"]')
    })

    // getBy... most recommended
    test('user-facing locators', async({page}) => {
        await page.getByRole('textbox', {name: 'Email'}).first().click()
        await page.getByRole('button', {name: 'Sign in'}).click()
        await page.getByLabel('Email').first().click()
        await page.getByPlaceholder('Jane Doe').click()
        await page.getByText('Auth').click()
        await page.getByTitle('IoT Dashboard').click()
        await page.getByTestId('SignIn').click() // data-testid
    })

    // .locator()
    test('locating child items', async({page}) => {
        await page.locator('nb-card nb-radio :text-is("Option 1")').click()
        await page.locator('nb-card').getByRole('button', {name: 'Sign in'}).click()
        // not recommended
        await page.locator('nb-card').nth(1).click()
    })

    test('locating parent elements', async({page}) => {
        await page.locator('nb-card', {hasText: "Using the Grid"}).getByRole('textbox', {name: 'Email'}).first().click()
        await page.locator('nb-card', {has: page.locator('#inputEmail1')}).getByRole('textbox', {name: 'Email'}).click()

        await page.locator('nb-card').filter({hasText: "Basic Form"}).getByRole('textbox', {name: 'Email'}).click()
        await page.locator('nb-card').filter({has: page.locator('.status-danger')}).getByRole('textbox', {name: 'Password'}).click()

        await page.locator('nb-card').filter({has: page.locator('nb-checkbox')}).filter({hasText: "Sign in"})
            .getByRole('textbox', {name: 'Email'}).click()

    })
})
