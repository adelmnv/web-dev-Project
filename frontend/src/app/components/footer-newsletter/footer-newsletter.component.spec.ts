import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FooterNewsletterComponent } from './footer-newsletter.component';

describe('FooterNewsletterComponent', () => {
  let component: FooterNewsletterComponent;
  let fixture: ComponentFixture<FooterNewsletterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FooterNewsletterComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FooterNewsletterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
