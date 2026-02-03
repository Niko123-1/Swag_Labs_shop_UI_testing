from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class FooterComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.footer = page.locator('[data-test="footer"]')
        self.social_twitter = page.locator('[data-test="social-twitter"]')
        self.social_facebook = page.locator('[data-test="social-facebook"]')
        self.social_linkedin = page.locator('[data-test="social-linkedin"]')
        self.footer_copy = page.locator('[data-test="footer-copy"]')

    def check_twitter_social_link(self):
        expect(self.social_twitter).to_have_attribute("href", "https://twitter.com/saucelabs")

    def check_facebook_social_link(self):
        expect(self.social_facebook).to_have_attribute("href", "https://www.facebook.com/saucelabs")

    def check_linkedin_social_link(self):
        expect(self.social_linkedin).to_have_attribute("href", "https://www.linkedin.com/company/sauce-labs/")

    def check_footer_info(self):
        expect(self.footer_copy).to_have_text("© 2026 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy")